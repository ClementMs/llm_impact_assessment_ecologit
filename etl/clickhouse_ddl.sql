CREATE TABLE llm_responses_ecologits_methodology  (

id Int64 PRIMARY KEY,
min_ghg_openai Decimal64(10), 
max_ghg_openai Decimal64(10), 
min_ghg_claude Decimal64(10),
max_ghg_claude Decimal64(10), 
min_energy_openai Decimal64(10), 
max_energy_openai Decimal64(10),
min_energy_claude Decimal64(10), 
max_energy_claude Decimal64(10), 
claude_response String,
openai_response String

)


