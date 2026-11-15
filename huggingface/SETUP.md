# Weekly Hugging Face updates

Source: https://github.com/Double-FW/EU-Web-Accessibility-Directive_EN301549

Destination: https://huggingface.co/datasets/GarethFW/Implementing_the_EU_Web_Accessibility_Directive_and_EN301549

The destination is fixed in export-config.json. No HF_DATASET_ID variable is needed.
Save a destination-scoped Hugging Face token as GitHub repository secret HF_TOKEN.
Create .github/workflows/huggingface-sync.yml from WORKFLOW_TO_COPY.txt in the
setup download. Run it manually once and check its result; weekly runs are
Mondays at 07:23 UTC. Never commit a token in a source file.

All approved source files are required; new/renamed documents need export-list
review. The RAG snapshot is document-only. Prompt records retain their execution
contract and matrix context. Exporting these sources does not execute a product
test, certify conformance, grant operational authority or reverify legal duties.
