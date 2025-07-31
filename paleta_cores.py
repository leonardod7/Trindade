import json

# Paleta de tons de azul para Trindade Medical
trindade_blue_palette = {
    "primary": "#003366",   # Azul escuro institucional
    "secondary": "#005B99", # Azul médio
    "accent": "#007ACC",    # Azul vibrante
    "light": "#66B2FF",     # Azul claro
    "extra_light": "#CCE6FF",# Azul muito claro
}

# Paleta de tons de cinza para Trindade Medical
tindade_gray_palette = {
    "dark": "#333333",    # Cinza escuro
    "medium_dark": "#666666", # Cinza médio escuro
    "medium": "#999999",      # Cinza médio
    "light": "#CCCCCC",       # Cinza claro
    "extra_light": "#F2F2F2"   # Cinza muito claro
}

# Salvar como arquivos JSON
with open("trindade_blue_palette.json", "w") as blue_file:
    json.dump(trindade_blue_palette, blue_file, indent=4)

with open("trindade_gray_palette.json", "w") as gray_file:
    json.dump(tindade_gray_palette, gray_file, indent=4)

print("Arquivos gerados: trindade_blue_palette.json e trindade_gray_palette.json")
