/** @type {import('next').NextConfig} */
const nextConfig = {
   //  basePath: '/',
   images: {
    domains: ['images.unsplash.com'],
  },
   eslint: {
    // Warning: This allows production builds to successfully complete even if
    // your project has ESLint errors.
    ignoreDuringBuilds: true,
  }
}

module.exports = nextConfig
