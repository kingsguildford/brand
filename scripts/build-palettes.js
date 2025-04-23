const fs = require('fs');
const { encode } = require('ase-utils');

// Read the brand.css file
const css = fs.readFileSync('brand.css', 'utf8');
const colorRegex = /--(.*?):\s*(#(?:[0-9a-fA-F]{3}){1,2})/g;
const matches = [...css.matchAll(colorRegex)];

// Mapping colors to name and hex value
const colors = matches.map(m => ({
  name: m[1].trim(),  // Color name
  hex: m[2].trim()    // Hex value
}));

console.log('Colors:', colors);

// Helper: Convert hex to [r, g, b] in 0-1 range
function hexToRgbArray(hex) {
  const cleanHex = hex.replace('#', '');
  const bigint = parseInt(cleanHex, 16);
  return [
    ((bigint >> 16) & 255) / 255,
    ((bigint >> 8) & 255) / 255,
    (bigint & 255) / 255
  ];
}

const aseSwatches = colors.map(c => {
  return {
    name: c.name,
    model: 'RGB',
    color: hexToRgbArray(c.hex),
    type: 'global'
  };
});

const asePath = 'palettes/kcg-brand-palette.ase';
const jsonPath = 'palettes/kcg-brand-palette.json';

// Write ASE file
try {
  const encodedSwatches = encode({ colors: aseSwatches });
  fs.writeFileSync(asePath, encodedSwatches);
  console.log(`✅ ASE file written to: ${asePath}`);
} catch (err) {
  console.error('❌ Error encoding ASE:', err);
}

// Write JSON file
try {
  fs.writeFileSync(jsonPath, JSON.stringify(colors, null, 2));
  console.log(`✅ JSON file written to: ${jsonPath}`);
} catch (err) {
  console.error('❌ Error writing JSON:', err);
}