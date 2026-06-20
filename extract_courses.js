const fs = require('fs');
const path = require('path');

const code = fs.readFileSync('courses.js', 'utf8');

// The file contains `const curriculum = ...;` and `const courseManifest = ...;`
// We will evaluate the code and export it.
const evalCode = code + '\nmodule.exports = { curriculum, courseManifest };';

let extracted;
try {
  const m = { exports: {} };
  const wrapper = new Function('module', 'exports', evalCode);
  wrapper(m, m.exports);
  extracted = m.exports;
} catch (e) {
  console.error("Failed to parse courses.js:", e);
  process.exit(1);
}

const { curriculum, courseManifest } = extracted;

fs.mkdirSync(path.join(__dirname, 'curriculum', 'tracks'), { recursive: true });
fs.writeFileSync(path.join(__dirname, 'curriculum', 'index.json'), JSON.stringify(curriculum, null, 2));

for (const trackName of Object.keys(curriculum)) {
  const trackObj = curriculum[trackName];
  const trackCourses = {};
  
  for (const tier of Object.keys(trackObj)) {
    const courseNames = trackObj[tier];
    for (const cName of courseNames) {
      if (courseManifest[cName]) {
        trackCourses[cName] = courseManifest[cName];
      }
    }
  }
  
  const filename = trackName.toLowerCase().replace(/[^a-z0-9]+/g, '_') + '.json';
  fs.writeFileSync(path.join(__dirname, 'curriculum', 'tracks', filename), JSON.stringify(trackCourses, null, 2));
}

console.log("Extraction complete.");
