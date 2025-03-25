import { config, initializeConfig } from './configModule.js';
initializeConfig("Alice");
console.log(`User configuration: ${config.user}`);