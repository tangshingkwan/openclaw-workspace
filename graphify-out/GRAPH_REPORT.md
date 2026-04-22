# Graph Report - /root/.openclaw/workspace  (2026-04-21)

## Corpus Check
- 21 files · ~2,131,443 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 182 nodes · 332 edges · 20 communities detected
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 68 edges (avg confidence: 0.56)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]

## God Nodes (most connected - your core abstractions)
1. `DataExporter` - 31 edges
2. `APIClient` - 27 edges
3. `DatabaseManager` - 27 edges
4. `SAPACProcessor` - 21 edges
5. `main()` - 12 edges
6. `main()` - 11 edges
7. `r()` - 9 edges
8. `load_graph()` - 9 edges
9. `p()` - 7 edges
10. `invoicingRow()` - 6 edges

## Surprising Connections (you probably didn't know these)
- `SAPACProcessor` --uses--> `APIClient`  [INFERRED]
  /root/.openclaw/workspace/synagie-pipeline/main.py → /root/.openclaw/workspace/synagie-pipeline/api_client.py
- `SAPACProcessor` --uses--> `DatabaseManager`  [INFERRED]
  /root/.openclaw/workspace/synagie-pipeline/main.py → /root/.openclaw/workspace/synagie-pipeline/database.py
- `SAPACProcessor` --uses--> `DataExporter`  [INFERRED]
  /root/.openclaw/workspace/synagie-pipeline/main.py → /root/.openclaw/workspace/synagie-pipeline/data_exporter.py
- `Format dates as Synagie API expects: 2025-11-01T00:00:00+08:00     Returns (date` --uses--> `APIClient`  [INFERRED]
  /root/.openclaw/workspace/synagie-pipeline/main.py → /root/.openclaw/workspace/synagie-pipeline/api_client.py
- `Get default date range for API queries.     - date_from: today - lookback_days (` --uses--> `APIClient`  [INFERRED]
  /root/.openclaw/workspace/synagie-pipeline/main.py → /root/.openclaw/workspace/synagie-pipeline/api_client.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.11
Nodes (25): APIClient, Send data to API endpoint, DataExporter, data_exporter.py - Export Synagie data to CEGID RETAIL flat file format, Convert any value to string safely., Convert to float string, return empty string if invalid., DatabaseManager, Truncate specified table (+17 more)

### Community 1 - "Community 1"
Cohesion: 0.11
Nodes (11): Export CEGID RETAIL rows to a flat file.          Args:             rows:, Legacy export — dispatches to appropriate format., Execute SELECT query and return results, Establish database connection, Close database connection, Create table with specified schema, Insert data into specified table, format_date_iso() (+3 more)

### Community 2 - "Community 2"
Cohesion: 0.11
Nodes (32): append_op(), append_schema(), create_entity(), create_relation(), delete_entity(), generate_id(), get_entity(), get_related() (+24 more)

### Community 3 - "Community 3"
Cohesion: 0.38
Nodes (11): blank(), buildContextParagraphs(), bulletP(), cell(), dataRow(), headerRow(), invoicingRow(), navyCell() (+3 more)

### Community 4 - "Community 4"
Cohesion: 0.33
Nodes (12): bfs_path(), build_adjacency(), communities(), export_context_block(), god_nodes(), inferred_edges(), load_graph(), main() (+4 more)

### Community 5 - "Community 5"
Cohesion: 0.2
Nodes (5): Fetch ALL Sales Orders with automatic pagination.          Returns:, Fetch After-Sale Orders from Synagie API.          Args:             vendor_code, Fetch ALL After-Sale Orders with automatic pagination.          Note: Synagie re, Fetch data from API endpoint, Fetch Sales Orders Report from Synagie API.          Args:             vendor_co

### Community 6 - "Community 6"
Cohesion: 0.2
Nodes (5): Transform a single sales order item into a CEGID RETAIL row.          Args:, Transform all sales orders (with products) into CEGID RETAIL rows.         One o, Transform a single aftersale product item into a CEGID RETAIL row.         Retur, Transform all aftersale orders into CEGID RETAIL rows., Convert ISO date string to YYYYMMDD format.

### Community 7 - "Community 7"
Cohesion: 0.6
Nodes (5): load_key(), main(), tavily_search(), to_brave_like(), to_markdown()

### Community 8 - "Community 8"
Cohesion: 1.0
Nodes (2): check_emails(), decode_str()

### Community 9 - "Community 9"
Cohesion: 1.0
Nodes (2): check_url(), main()

### Community 10 - "Community 10"
Cohesion: 0.67
Nodes (2): parse_bookmarks_html(), Parse Chrome bookmarks HTML recursively.

### Community 11 - "Community 11"
Cohesion: 0.67
Nodes (1): handler()

### Community 12 - "Community 12"
Cohesion: 1.0
Nodes (0): 

### Community 13 - "Community 13"
Cohesion: 1.0
Nodes (0): 

### Community 14 - "Community 14"
Cohesion: 1.0
Nodes (0): 

### Community 15 - "Community 15"
Cohesion: 1.0
Nodes (0): 

### Community 16 - "Community 16"
Cohesion: 1.0
Nodes (0): 

### Community 17 - "Community 17"
Cohesion: 1.0
Nodes (0): 

### Community 18 - "Community 18"
Cohesion: 1.0
Nodes (0): 

### Community 19 - "Community 19"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **37 isolated node(s):** `Fetch data from API endpoint`, `Send data to API endpoint`, `Fetch Sales Orders Report from Synagie API.          Args:             vendor_co`, `Fetch ALL Sales Orders with automatic pagination.          Returns:`, `Fetch After-Sale Orders from Synagie API.          Args:             vendor_code` (+32 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 12`** (2 nodes): `fetchCreator()`, `patreon_fetch.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (2 nodes): `fetchPosts()`, `patreon-fetch.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (2 nodes): `seed-ontology.py`, `ts()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 15`** (2 nodes): `categorize()`, `categorize-bookmarks.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (2 nodes): `fetchAllPosts()`, `patreon-fetch-week.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 17`** (1 nodes): `patreon_scrape.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 18`** (1 nodes): `config.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (1 nodes): `switch-resolution.ps1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DataExporter` connect `Community 0` to `Community 1`, `Community 6`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **Why does `APIClient` connect `Community 0` to `Community 1`, `Community 5`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **Why does `DatabaseManager` connect `Community 0` to `Community 1`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `DataExporter` (e.g. with `SAPACProcessor` and `Format dates as Synagie API expects: 2025-11-01T00:00:00+08:00     Returns (date`) actually correct?**
  _`DataExporter` has 19 INFERRED edges - model-reasoned connections that need verification._
- **Are the 19 inferred relationships involving `APIClient` (e.g. with `SAPACProcessor` and `Format dates as Synagie API expects: 2025-11-01T00:00:00+08:00     Returns (date`) actually correct?**
  _`APIClient` has 19 INFERRED edges - model-reasoned connections that need verification._
- **Are the 19 inferred relationships involving `DatabaseManager` (e.g. with `SAPACProcessor` and `Format dates as Synagie API expects: 2025-11-01T00:00:00+08:00     Returns (date`) actually correct?**
  _`DatabaseManager` has 19 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `SAPACProcessor` (e.g. with `APIClient` and `DatabaseManager`) actually correct?**
  _`SAPACProcessor` has 3 INFERRED edges - model-reasoned connections that need verification._