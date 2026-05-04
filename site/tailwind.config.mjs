/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}"],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        // Pylon brand palette per ../BRAND.md
        pylon: {
          blue: "#1F3D7A",
          black: "#0D1014",
          surface: "#FFFFFF",
          "surface-dim": "#F5F6F8",
          "surface-dark": "#13161B",
          "surface-dark-dim": "#1B1F26",
          amber: "#E89236",
          red: "#C8473D",
          green: "#4F8F5A",
          slate: "#7B8794",
        },
      },
      fontFamily: {
        // Söhne is licensed (per BRAND.md). System-stack fallback ships in MVP.
        sans: ["system-ui", "-apple-system", '"Segoe UI"', "Helvetica", "Arial", "sans-serif"],
        mono: ["ui-monospace", "SFMono-Regular", "Menlo", "Consolas", "monospace"],
      },
      typography: {
        DEFAULT: {
          css: {
            "code::before": { content: '""' },
            "code::after": { content: '""' },
            maxWidth: "none",
          },
        },
      },
    },
  },
  plugins: [],
};
