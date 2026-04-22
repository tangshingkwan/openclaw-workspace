#!/usr/bin/env python3
"""Cluster analysis for Y2 Wiki graph."""
import json
from collections import defaultdict

GRAPH_FILE = '/root/.openclaw/workspace/wiki/graphify-out/graph.json'
with open(GRAPH_FILE) as f:
    g = json.load(f)

nodes = g['nodes']
edges = g['edges']

# Degree analysis
out_degree = defaultdict(int)
in_degree  = defaultdict(int)
for e in edges:
    out_degree[e['source']] += 1
    in_degree[e['target']]  += 1

# Simple label-propagation community detection
adj = defaultdict(set)
for e in edges:
    adj[e['source']].add(e['target'])
    adj[e['target']].add(e['source'])

node_ids = [n['id'] for n in nodes]
labels = {nid: i for i, nid in enumerate(node_ids)}

def spread_labels(iterations=5):
    for _ in range(iterations):
        new_labels = dict(labels)
        for node_id in adj:
            neighbor_labels = [labels[n] for n in adj[node_id] if n in labels]
            if neighbor_labels:
                new_labels[node_id] = max(set(neighbor_labels), key=neighbor_labels.count)
        labels.update(new_labels)

spread_labels()

communities = defaultdict(list)
for nid, cid in labels.items():
    communities[cid].append(nid)

print(f'Communities: {len(communities)}')

node_type = {n['id']: n.get('type', 'unknown') for n in nodes}

comm_types = defaultdict(lambda: defaultdict(int))
for cid, members in communities.items():
    for m in members:
        comm_types[cid][node_type.get(m, 'unknown')] += 1

# Top hubs and authorities
hubs = sorted(out_degree.items(), key=lambda x: -x[1])[:15]
authorities = sorted(in_degree.items(), key=lambda x: -x[1])[:15]

print('\nTop Hub Nodes (out-degree):')
for nid, d in hubs:
    print(f'  {nid}: {d}')

print('\nTop Authority Nodes (in-degree):')
for nid, d in authorities:
    print(f'  {nid}: {d}')

print('\nCommunity summary:')
for cid, members in sorted(communities.items(), key=lambda x: -len(x[1])):
    total = len(members)
    types = comm_types[cid]
    top_types = sorted(types.items(), key=lambda x: -x[1])[:4]
    print(f'  C{cid} ({total} nodes): {[(t, c) for t, c in top_types]}')
    print(f'    Sample: {sorted(members)[:6]}')

# Type distribution
type_dist = defaultdict(int)
for n in nodes:
    type_dist[n.get('type', 'unknown')] += 1

print('\nType distribution:')
for t, c in sorted(type_dist.items(), key=lambda x: -x[1]):
    print(f'  {t}: {c}')

# Save summary
summary = {
    'total_nodes': len(nodes),
    'total_edges': len(edges),
    'communities': {cid: sorted(members) for cid, members in communities.items()},
    'comm_sizes': {cid: len(members) for cid, members in communities.items()},
    'comm_type_summary': {str(cid): dict(sorted(types.items(), key=lambda x: -x[1])[:5])
                          for cid, types in comm_types.items()},
    'top_hubs': hubs,
    'top_authorities': authorities,
    'type_distribution': dict(sorted(type_dist.items(), key=lambda x: -x[1])),
}

with open('/root/.openclaw/workspace/wiki/graphify-out/clustering_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)
print('\nClustering summary saved.')
