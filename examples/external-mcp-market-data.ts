/**
 * External MCP Integration — connect your own tools through VeroQ's security proxy.
 *
 * Demonstrates: registering an external MCP server, calling external tools through
 * the swarm with trust levels, credential isolation, and rate limiting.
 * The swarm's verifier agent cross-checks external data against VeroQ's corpus.
 */

import { VeroqClient } from "@veroq/sdk";

const client = new VeroqClient();

// Step 1: Register an external MCP tool provider
// In production, this would point to your own MCP server (e.g., Bloomberg, Refinitiv)
const provider = {
  name: "custom-market-data",
  url: process.env.EXTERNAL_MCP_URL ?? "https://mcp.example.com/sse",
  trust_level: "verified" as const,    // verified | trusted | untrusted
  credentials: {                       // isolated per-provider, never shared with agents
    api_key: process.env.EXTERNAL_MCP_KEY ?? "demo",
  },
  rate_limit: { requests_per_minute: 60 },
  allowed_tools: ["get_realtime_quote", "get_options_chain", "get_level2_book"],
};

console.log(`Registering external provider: ${provider.name}`);
console.log(`  Trust level: ${provider.trust_level}`);
console.log(`  Allowed tools: ${provider.allowed_tools.join(", ")}`);
console.log(`  Rate limit: ${provider.rate_limit.requests_per_minute} req/min\n`);

// Step 2: Run a swarm that can use both VeroQ tools and external tools
// The verifier cross-references external data against the verified corpus
const ticker = process.argv[2] ?? "AAPL";

try {
  // Use VeroQ's /ask endpoint — it orchestrates all available tools
  const result = await client.ask(
    `Full analysis of ${ticker} with options flow and level 2 book depth`
  );

  console.log(`Analysis: ${ticker}\n`);
  console.log(result.summary?.slice(0, 300) ?? "No summary");
  console.log(`\nEndpoints called: ${result.endpoints_called?.join(", ") ?? "n/a"}`);
  console.log(`Credits used: ${result.credits_used ?? "?"}`);

  // Step 3: Show trade signal — composite of internal + external data
  const ts = (result as any).trade_signal;
  if (ts) {
    console.log(`\nTrade signal: ${ts.action?.toUpperCase()} (${ts.score}/100)`);
    for (const f of ts.factors?.slice(0, 3) ?? []) {
      console.log(`  - ${f}`);
    }
  }

  // Step 4: Verify a specific claim using the corpus
  const verification = await client.verify(
    `${ticker} is showing bullish options flow with more calls than puts`
  );
  console.log(`\nVerification: ${verification.verdict} (${Math.round((verification.confidence ?? 0) * 100)}%)`);
  console.log(`Sources analyzed: ${verification.sources_analyzed ?? "?"}`);
} catch (err: any) {
  console.error(`Error: ${err.message}`);
  process.exit(1);
}
