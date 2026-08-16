# Legacy Artifact Status

The current HTML artifacts (e.g., located in `visualisations/` and `_archive/`) have been classified as follows:

1. **Status:** Retained as Archive. They are evidence-view only and serve as historical process documentation and interaction references.
2. **Editability:** Not editable. Do not edit these files to reflect new semantic data.
3. **Relevance:** Superseded. They were built on the old, mechanical metric-centric schema (`nalex_viz_schema.json`) which lacks the semantic depth required for current goals.
4. **Base Suitability:** Not suitable as a base for reflective rebuild. The underlying HTML structure was designed for flat metric presentation and does not support the multi-layered `reflective_schema` (evidence samples, limits, reflection prompts).

**Recommendation:**
New reflective artifacts must **start fresh** in the `./artifacts/viz/` or `./artifacts/reflective/` directories using entirely new templates designed to consume the `nalex_viz_projection_contract.json` and `nalex_reflective_schema_contract.json` formats. Do not edit legacy artifacts in place.
