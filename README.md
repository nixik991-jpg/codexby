# codexby

This repository contains a generated starter dataset for car makes/models covering the requested 2005–2025 range.

## Files

- `output/car_models_2005_2025.csv`: CSV with the required output schema, example rows, and one placeholder row per requested make.
- `scripts/build_car_dataset_stub.py`: Rebuilds the CSV structure.

## Notes

The execution environment blocked outbound data-source calls with HTTP 403 responses, so a fully comprehensive make/model/variant extraction could not be completed from authoritative online catalogs in this run.
