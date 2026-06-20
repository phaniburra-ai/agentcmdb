const API_KEY = 'dev-agentcmdb-key';

async function loadAgents() {
  const q = document.getElementById('search')?.value || '';
  const res = await fetch('/api/agents?q=' + encodeURIComponent(q));
  const agents = await res.json();
  document.getElementById('agents').innerHTML = agents.map(a => `
    <tr>
      <td><strong>${a.name}</strong><br/><small>${a.description || ''}</small></td>
      <td>${a.owner}<br/><small>${a.business_unit || ''}</small></td>
      <td>${a.environment}</td>
      <td><span class="badge ${a.risk_level}">${a.risk_level}</span></td>
      <td>${a.lifecycle_state}</td>
      <td>${a.model_provider || ''} ${a.model_name || ''}<br/><small>${a.framework || ''}</small></td>
    </tr>`).join('');
  loadCosts();
}

async function loadCosts() {
  const res = await fetch('/api/costs/summary');
  const costs = await res.json();
  document.getElementById('costs').innerHTML = costs.map(c => `
    <tr>
      <td>${c.agent_name}</td>
      <td>${c.total_input_tokens}</td>
      <td>${c.total_output_tokens}</td>
      <td>$${Number(c.total_cost_usd).toFixed(4)}</td>
      <td>${c.event_count}</td>
    </tr>`).join('');
}

async function createAgent() {
  const payload = {
    name: document.getElementById('name').value,
    owner: document.getElementById('owner').value,
    business_unit: document.getElementById('business_unit').value,
    environment: document.getElementById('environment').value,
    framework: document.getElementById('framework').value,
    model_provider: document.getElementById('model_provider').value,
    model_name: document.getElementById('model_name').value,
    risk_level: document.getElementById('risk_level').value,
    lifecycle_state: 'draft',
    criticality: document.getElementById('risk_level').value,
    description: document.getElementById('description').value,
    data_sources: [], tools: [], actions: [], tags: []
  };
  const res = await fetch('/api/agents', {
    method:'POST', headers:{'Content-Type':'application/json', 'x-api-key':API_KEY}, body:JSON.stringify(payload)
  });
  if (!res.ok) alert('Failed to create agent');
  loadAgents();
}

loadAgents();
