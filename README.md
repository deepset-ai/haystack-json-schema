# JSON Schema for Haystack Pipeline YAML files

<p align="center" float="left">
  <img alt="" src="https://raw.githubusercontent.com/deepset-ai/.github/main/deepset-logo-colored.png" width="30%"/>
  <img alt="" src="https://raw.githubusercontent.com/deepset-ai/.github/main/haystack-logo-colored-on-dark.png#gh-dark-mode-only" width="30%"/>
  <img alt="" src="https://raw.githubusercontent.com/deepset-ai/.github/main/haystack-logo-colored.png#gh-light-mode-only" width="30%"/>
</p>

<a href="https://github.com/deepset-ai/haystack-json-schema/actions/workflows/schemas.yml">
    <img alt="Schemas" src="https://github.com/deepset-ai/haystack-json-schema/actions/workflows/schemas.yml/badge.svg">
</a>

JSON Schema for validating [Haystack](https://haystack.deepset.ai/) [Pipeline YAML files](https://docs.haystack.deepset.ai/docs/pipelines#yaml-file-definitions). These schemas are [referenced in SchemaStore](https://www.schemastore.org/json/) and allow IDEs to validate your Haystack Pipeline YAML files.

**These schemas are all generated. PRs on this repo are not monitored and will be ignored. In case of problems, open an issue or discussion on the [main Haystack repository](https://github.com/deepset-ai/haystack).**

Technical implementation:
- Schemas are generated using the [official Haystack Docker images](https://hub.docker.com/r/deepset/haystack), matching the image tag with the release provided (or `main` for the unstable version).
- The workflow starts when this repo receives a disapatch event, either triggered from the haystack repository every time a new Docker image is published, or running the workflow manually.
- The desired Haystack version is contained in the dispatch event itself.
- The `main` schema is only updated when the Haystack release is `main`, allowing to update schemas for any release without disrupting the unstable version (this is handy to fix any issue we might have with the CI).
