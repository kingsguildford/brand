const fs = require('fs');
const { encode } = require('ase-utils');

const css = fs.readFileSync('brand.css', 'utf8');
const colorRegex = /--(.*?):\s*(#(?:[0-9a-fA-F]{3}){1,2})/g;
const matches = [...css.matchAll(colorRegex)];
const colors = matches.map(m => ({ name: m[1].trim(), hex: m[2].trim() }));

fs.writeFileSync('palettes/brand-palette.json', JSON.stringify(colors, null, 2));

function hexToRgb(hex) {
  hex = hex.replace('#', '');
  return [
    parseInt(hex.substring(0, 2), 16),
    parseInt(hex.substring(2, 4), 16),
    parseInt(hex.substring(4, 6), 16)
  ];
}

const aseSwatches = colors.map(c => ({
  name: c.name,
  model: 'RGB',
  color: hexToRgb(c.hex)
}));

const buffer = encode({ groups: [{ name: 'Brand', colors: aseSwatches }] });
fs.writeFileSync('palettes/brand-palette.ase', buffer);
