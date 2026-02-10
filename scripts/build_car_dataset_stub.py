"""Builds a starter CSV for the requested 2005-2025 make/model dataset.

This environment cannot access external automotive databases (HTTP 403),
so the script creates a structured starter file with target makes and
example rows in the requested schema.
"""

from __future__ import annotations

import csv
from pathlib import Path

columns = [
    "Make",
    "Model",
    "Trim/Variant",
    "Generation/Chassis Code",
    "Years of Production",
    "Displacement",
    "Cylinder Configuration",
    "Power",
]

makes = [
    "Alfa Romeo",
    "Audi",
    "BMW",
    "CUPRA",
    "Fiat",
    "Ford",
    "Honda",
    "Hyundai",
    "Jaguar",
    "Kia",
    "Land Rover",
    "Mazda",
    "Mercedes",
    "Mini",
    "Nissan",
    "Peugeot",
    "Porsche",
    "Renault",
    "Seat",
    "Vauxhall",
    "Toyota",
    "Volkswagen",
    "Volvo",
]

example_rows = [
    ["BMW", "1 Series", "116i", "E81/E82/E87/E88", "2004–2011", "1.6–2.0L", "I4", "114–127 hp"],
    ["BMW", "1 Series", "118i", "F20/F21", "2012–2019", "1.6–2.0L", "I4", "125–170 hp"],
    ["Audi", "A3", "1.6 TDI", "8P", "2005–2013", "1.6L", "I4 Diesel", "105 hp"],
    ["Fiat", "Panda", "1.2", "169", "2005–2012", "1.2L", "I4", "60–75 hp"],
]

out = Path("output/car_models_2005_2025.csv")
out.parent.mkdir(parents=True, exist_ok=True)

with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(columns)
    for row in example_rows:
        w.writerow(row)
    for make in makes:
        w.writerow([make, "", "", "", "2005–2025", "", "", ""])

print(f"Wrote {out}")
