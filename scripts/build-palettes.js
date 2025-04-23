const fs = require('fs');
const path = require('path');

const css = fs.readFileSync('brand.css', 'utf8');
const colorRegex = /--(.*?):\s*(#(?:[0-9a-fA-F]{3}){1,2})/g;
const matches = [...css.matchAll(colorRegex)];
const colors = matches.map(m => ({ name: m[1].trim(), hex: m[2].trim() }));

// Output JSON
fs.writeFileSync('palettes/brand-palette.json', JSON.stringify(colors, null, 2));

// Output ASE
const { encode } = require('@theapprenticewizard/ase-utils');
const aseSwatches = colors.map(c => ({
  name: c.name,
  color: c.hex,
  model: 'RGB',
  type: 'global',
}));
const buffer = encode(aseSwatches);
fs.writeFileSync('palettes/brand-palette.ase', buffer);
