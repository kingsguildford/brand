const fs = require('fs');

const css = fs.readFileSync('brand.css', 'utf8');
const colorRegex = /--(.*?):\s*(#(?:[0-9a-fA-F]{3}){1,2})/g;
const matches = [...css.matchAll(colorRegex)];
const colors = matches.map(m => ({ name: m[1].trim(), hex: m[2].trim() }));

fs.writeFileSync('palettes/brand-palette.json', JSON.stringify(colors, null, 2));
