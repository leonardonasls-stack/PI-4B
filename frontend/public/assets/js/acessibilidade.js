// Controles de acessibilidade compartilhados (Alto Contraste e A-/A+) — WCAG 2.1
(function () {
  window.alternarAltoContraste = function () {
    const ativo = document.body.classList.toggle("high-contrast-mode");
    localStorage.setItem("alto_contraste", ativo ? "1" : "0");
    document.body.style.filter = ativo ? "contrast(1.25)" : "";
  };

  let tamanhoFonteBase = parseInt(localStorage.getItem("tamanho_fonte_base") || "100", 10);
  window.alterarTamanhoFonte = function (delta) {
    tamanhoFonteBase = Math.min(140, Math.max(85, tamanhoFonteBase + delta * 10));
    document.documentElement.style.fontSize = tamanhoFonteBase + "%";
    localStorage.setItem("tamanho_fonte_base", String(tamanhoFonteBase));
  };

  function aplicarPreferenciasSalvas() {
    if (localStorage.getItem("alto_contraste") === "1" && document.body) {
      document.body.classList.add("high-contrast-mode");
      document.body.style.filter = "contrast(1.25)";
    }
    const salvo = localStorage.getItem("tamanho_fonte_base");
    if (salvo) {
      document.documentElement.style.fontSize = salvo + "%";
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", aplicarPreferenciasSalvas);
  } else {
    aplicarPreferenciasSalvas();
  }
})();
