// Prompts
// You are a coding assistant which specializes in Javascript and Express.js framework
// Help me improve the following code that i have provided. Before you gave me an answer think step by step and after that give me the answer and list down the improvement you made in bullet form
// Improve the code and make it secure. Limit the improvements to 5 if possible
// Output
// Alright! Let's focus on improving your Express.js app while keeping it secure and limiting it to 5 meaningful enhancements. I’ll first explain each improvement, then give you the updated code.

// 🔐 Top 5 Security-Focused Improvements:
// Use helmet middleware
// ➤ Sets various HTTP headers to help secure your app (e.g., against XSS, clickjacking).

// Disable x-powered-by header
// ➤ Express adds this header by default, revealing that the app uses Express — better to hide it.

// Rate limiting with express-rate-limit
// ➤ Prevents brute-force attacks and abuse by limiting repeated requests.

// Sanitize input with express-mongo-sanitize
// ➤ Prevents MongoDB operator injection if you plan to use MongoDB.

// Load environment variables securely
// ➤ Use dotenv to keep sensitive values (e.g., port, secrets) outside the source code.



const express = require('express');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const mongoSanitize = require('express-mongo-sanitize');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Security middleware
app.use(helmet());
app.use(mongoSanitize());
app.disable('x-powered-by');

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Routes
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Start server
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});

// 🛠️ Summary of Improvements:
// ✅ Helmet: Protects from common web vulnerabilities.

// ✅ mongoSanitize: Guards against injection if you're using MongoDB.

// ✅ Rate Limiting: Prevents abuse or brute-force attempts.

// ✅ Hide Express signature: Removes x-powered-by header.

// ✅ Environment variables: Securely handle config with dotenv.

// Would you like help adding CORS rules or input validation next?