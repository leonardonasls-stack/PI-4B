// Configuração compartilhada de tokens MD3 do Tailwind CSS (Portal & Admin)
(function () {
  const origWarn = console.warn;
  console.warn = function (...args) {
    if (
      args[0] &&
      typeof args[0] === "string" &&
      args[0].includes("cdn.tailwindcss.com should not be used in production")
    ) {
      return;
    }
    origWarn.apply(console, args);
  };

  const fontStack = ["Public Sans", "system-ui", "-apple-system", "sans-serif"];

  if (typeof tailwind !== "undefined") {
    tailwind.config = {
      darkMode: "class",
      theme: {
        extend: {
          colors: {
            "on-tertiary-fixed-variant": "#6e3900",
            "on-error-container": "#93000a",
            "error-container": "#ffdad6",
            "primary-container": "#0e3b4a",
            "inverse-on-surface": "#ecf1ff",
            "outline-variant": "#c1c7cb",
            "on-surface": "#111c2d",
            surface: "#f9f9ff",
            "surface-container-low": "#f0f3ff",
            "on-primary-fixed": "#001f29",
            "primary-fixed-dim": "#a4cddf",
            "on-background": "#111c2d",
            "tertiary-fixed-dim": "#ffb77d",
            "on-primary-container": "#7da5b7",
            "on-surface-variant": "#41484b",
            "surface-bright": "#f9f9ff",
            "on-secondary-container": "#00714e",
            "secondary-fixed": "#85f8c4",
            "secondary-fixed-dim": "#68dba9",
            "on-secondary-fixed-variant": "#005137",
            "surface-tint": "#3c6474",
            secondary: "#006c4a",
            "on-primary": "#ffffff",
            "tertiary-fixed": "#ffdcc3",
            "on-secondary": "#ffffff",
            "primary-fixed": "#c0e9fc",
            background: "#f9f9ff",
            primary: "#002530",
            tertiary: "#371900",
            outline: "#71787c",
            "inverse-surface": "#263143",
            "tertiary-container": "#562b00",
            "on-primary-fixed-variant": "#234c5b",
            "surface-variant": "#d8e3fb",
            "surface-container-high": "#dee8ff",
            "inverse-primary": "#a4cddf",
            "surface-container-lowest": "#ffffff",
            "on-error": "#ffffff",
            "on-tertiary-fixed": "#2f1500",
            "on-tertiary": "#ffffff",
            "on-tertiary-container": "#eb851c",
            "surface-dim": "#cfdaf2",
            "secondary-container": "#82f5c1",
            "on-secondary-fixed": "#002114",
            error: "#ba1a1a",
            "surface-container": "#e7eeff",
            "surface-container-highest": "#d8e3fb",
          },
          borderRadius: {
            DEFAULT: "0.25rem",
            lg: "0.5rem",
            xl: "0.75rem",
            full: "9999px",
          },
          spacing: {
            margin: "2rem",
            "space-2xl": "3rem",
            "space-md": "1rem",
            "gutter-sm": "1rem",
            "space-lg": "1.5rem",
            "space-xl": "2rem",
            gutter: "1.5rem",
            "space-sm": "0.5rem",
            "space-xs": "0.25rem",
            "margin-sm": "1rem",
          },
          fontFamily: {
            sans: fontStack,
            "headline-sm": fontStack,
            "display-lg-mobile": fontStack,
            "label-sm": fontStack,
            "headline-md": fontStack,
            "label-lg": fontStack,
            "headline-xl-mobile": fontStack,
            "body-lg": fontStack,
            "label-md": fontStack,
            "body-md": fontStack,
            "display-lg": fontStack,
            "body-sm": fontStack,
            "headline-lg": fontStack,
            "headline-xl": fontStack,
          },
          fontSize: {
            "headline-sm": ["18px", { lineHeight: "26px", letterSpacing: "0em", fontWeight: "600" }],
            "display-lg-mobile": ["32px", { lineHeight: "40px", letterSpacing: "-0.01em", fontWeight: "800" }],
            "label-sm": ["12px", { lineHeight: "16px", letterSpacing: "0.04em", fontWeight: "700" }],
            "headline-md": ["22px", { lineHeight: "28px", letterSpacing: "0em", fontWeight: "600" }],
            "label-lg": ["16px", { lineHeight: "24px", letterSpacing: "0.01em", fontWeight: "600" }],
            "headline-xl-mobile": ["26px", { lineHeight: "34px", letterSpacing: "-0.01em", fontWeight: "700" }],
            "body-lg": ["18px", { lineHeight: "28px", letterSpacing: "0em", fontWeight: "400" }],
            "label-md": ["14px", { lineHeight: "20px", letterSpacing: "0.01em", fontWeight: "600" }],
            "body-md": ["16px", { lineHeight: "24px", letterSpacing: "0em", fontWeight: "400" }],
            "display-lg": ["48px", { lineHeight: "56px", letterSpacing: "-0.02em", fontWeight: "800" }],
            "body-sm": ["14px", { lineHeight: "20px", letterSpacing: "0.01em", fontWeight: "400" }],
            "headline-lg": ["28px", { lineHeight: "36px", letterSpacing: "-0.01em", fontWeight: "700" }],
            "headline-xl": ["36px", { lineHeight: "44px", letterSpacing: "-0.02em", fontWeight: "700" }],
          },
        },
      },
    };
  }
})();
