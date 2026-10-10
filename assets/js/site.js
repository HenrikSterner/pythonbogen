(() => {
  "use strict";

  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
  const text = (selector, value, root = document) => {
    const node = $(selector, root);
    if (node) node.textContent = value;
  };
  const readJSON = async (path) => {
    const response = await fetch(path);
    if (!response.ok) throw new Error(`Kunne ikke hente ${path} (${response.status})`);
    return response.json();
  };

  function initMenu() {
    const toggle = $(".menu-toggle");
    const nav = $(".primary-nav");
    if (!toggle || !nav) return;
    const setOpen = (open) => {
      nav.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", String(open));
      const label = $(".menu-label", toggle);
      const icon = $(".menu-icon", toggle);
      if (label) label.textContent = open ? "Luk" : "Menu";
      if (icon) icon.textContent = open ? "×" : "☰";
    };
    toggle.addEventListener("click", () => setOpen(toggle.getAttribute("aria-expanded") !== "true"));
    nav.addEventListener("click", (event) => {
      if (event.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setOpen(false);
        toggle.focus();
      }
    });
    window.addEventListener("resize", () => {
      if (window.innerWidth > 760) setOpen(false);
    });
  }

  function initCodeDemo() {
    const root = $("[data-code-demo]");
    if (!root) return;
    const names = ["Sara", "Ali", "Emil", "Freja"];
    let step = 0;
    const output = $("[data-demo-output]", root);
    const status = $("[data-demo-status]", root);
    const next = $("[data-demo-next]", root);
    const reset = $("[data-demo-reset]", root);
    const update = () => {
      if (step === 0) output.textContent = "Tryk på »Vis næste trin«. ";
      else output.textContent = `Hej ${names[step - 1]}`;
      status.textContent = `${step} af ${names.length} hilsner`;
      next.textContent = step >= names.length ? "Alle fire trin vist" : "Vis næste trin";
      next.disabled = step >= names.length;
      next.setAttribute("aria-label", step < names.length ? `Vis trin ${step + 1} af ${names.length}` : "Alle fire hilsner er vist");
    };
    next.addEventListener("click", () => {
      if (step < names.length) step += 1;
      update();
    });
    reset.addEventListener("click", () => {
      step = 0;
      update();
      next.focus();
    });
    update();
  }

  function initChapterSearch() {
    const input = $("#chapter-search");
    const cards = $$("[data-chapter-card]");
    const count = $("[data-chapter-count]");
    const empty = $("[data-chapter-empty]");
    if (!input || !cards.length) return;
    const run = () => {
      const query = input.value.trim().toLocaleLowerCase("da");
      let visible = 0;
      for (const card of cards) {
        const match = card.dataset.search.toLocaleLowerCase("da").includes(query);
        card.hidden = !match;
        if (match) visible += 1;
      }
      if (count) count.textContent = `${visible} af ${cards.length} kapitler`;
      if (empty) empty.hidden = visible > 0;
    };
    input.addEventListener("input", run);
  }

  function initLabs() {
    const cards = $$("[data-lab-card]");
    const search = $("#lab-search");
    const topic = $("#lab-topic");
    const level = $("#lab-level");
    const count = $("[data-lab-count]");
    const empty = $("[data-lab-empty]");
    if (!cards.length) return;

    const params = new URLSearchParams(location.search);
    const initialTopic = params.get("topic");
    if (topic && [...topic.options].some((option) => option.value === initialTopic)) topic.value = initialTopic;
    if (search) search.value = params.get("search") || "";

    const run = (changeURL = true) => {
      const query = (search?.value || "").trim().toLocaleLowerCase("da");
      const selectedTopic = topic?.value || "alle";
      const selectedLevel = level?.value || "alle";
      let visible = 0;
      for (const card of cards) {
        const topics = card.dataset.topics.split(/\s+/);
        const levels = card.dataset.level.toLocaleLowerCase("da");
        const matches = (!query || card.dataset.search.toLocaleLowerCase("da").includes(query))
          && (selectedTopic === "alle" || topics.includes(selectedTopic))
          && (selectedLevel === "alle" || levels.includes(selectedLevel.toLocaleLowerCase("da")));
        card.hidden = !matches;
        if (matches) visible += 1;
      }
      if (count) count.textContent = `${visible} ${visible === 1 ? "laboratorium" : "laboratorier"}`;
      if (empty) empty.hidden = visible > 0;
      if (changeURL && history.replaceState) {
        const nextParams = new URLSearchParams();
        if (query) nextParams.set("search", query);
        if (selectedTopic !== "alle") nextParams.set("topic", selectedTopic);
        if (selectedLevel !== "alle") nextParams.set("level", selectedLevel);
        history.replaceState(null, "", `${location.pathname}${nextParams.size ? `?${nextParams}` : ""}${location.hash}`);
      }
    };
    search?.addEventListener("input", () => run());
    topic?.addEventListener("change", () => run());
    level?.addEventListener("change", () => run());
    $$('[data-lab-reset]').forEach((button) => button.addEventListener("click", () => {
      if (search) search.value = "";
      if (topic) topic.value = "alle";
      if (level) level.value = "alle";
      run();
      search?.focus();
    }));
    run(false);
  }

  function initScenarios() {
    const message = $("[data-student-message]");
    const answer = $("[data-tutor-message]");
    const scenarios = {
      loop: [
        "Hvorfor bliver alle navnene skrevet ud?",
        "Listen har flere navne. Løkken tager ét navn ad gangen, og print skriver en hilsen til det navn. Hvilket navn står i elev på første omgang?",
      ],
      error: [
        "Jeg får NameError: navn is not defined. Hvad betyder det?",
        "Python møder et navn, den ikke kan finde en værdi for. Kig på stavningen i linjen med fejlen: hvor opretter du variablen, og bruger du samme navn begge steder?",
      ],
      improve: [
        "Jeg kan få listen skrevet ud. Hvordan forklarer jeg løkken?",
        "Beskriv først, hvad værdien af elev er i første omgang. Følg derefter hvordan løkken vælger næste navn, og hvorfor kroppen kører igen.",
      ],
    };
    $$('[data-scenario]').forEach((button) => button.addEventListener("click", () => {
      $$('[data-scenario]').forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
      const pair = scenarios[button.dataset.scenario];
      if (pair && message && answer) [message.textContent, answer.textContent] = pair;
    }));
  }

  function initLightbox() {
    const dialog = $("[data-lightbox-dialog]");
    const image = $("[data-lightbox-image]");
    if (!dialog || !image || typeof dialog.showModal !== "function") return;
    let trigger = null;
    $$('[data-lightbox]').forEach((button) => button.addEventListener("click", () => {
      trigger = button;
      image.src = button.dataset.lightbox;
      image.alt = $("img", button)?.alt || "Forstørret billede";
      dialog.showModal();
      $("[data-lightbox-close]", dialog)?.focus();
    }));
    const close = () => {
      dialog.close();
      if (trigger?.isConnected) trigger.focus();
    };
    $("[data-lightbox-close]", dialog)?.addEventListener("click", close);
    dialog.addEventListener("click", (event) => {
      if (event.target === dialog) close();
    });
    dialog.addEventListener("close", () => {
      image.removeAttribute("src");
      if (trigger?.isConnected) trigger.focus();
    });
  }

  function initReader() {
    const articles = $$("[data-book-content]");
    if (!articles.length) return;
    const entries = [
      { key: "forord", path: "laeseproeve/kapitler/forord.html", label: "Forord" },
      { key: "chapter", path: "laeseproeve/kapitler/01-dit-foerste-program.html", label: "Dit første program" },
    ];
    for (const entry of entries) {
      const article = $(`[data-${entry.key}]`);
      fetch(entry.path)
        .then((response) => {
          if (!response.ok) throw new Error("Prøven kunne ikke indlæses.");
          return response.text();
        })
        .then((markup) => { article.innerHTML = markup; })
        .catch(() => {
          article.textContent = "Teksten kunne ikke indlæses. Start hjemmesiden med en lokal HTTP-server som beskrevet i README.";
        });
    }
    const buttons = $$('[data-sample]');
    const update = (key) => {
      const entry = entries.find((item) => item.key === key) || entries[0];
      buttons.forEach((button) => {
        const current = button.dataset.sample === entry.key;
        button.classList.toggle("is-active", current);
        if (current) button.setAttribute("aria-current", "true");
        else button.removeAttribute("aria-current");
      });
      articles.forEach((article) => { article.hidden = !article.hasAttribute(`data-${entry.key}`); });
      text("[data-reader-title]", entry.label);
    };
    buttons.forEach((button) => button.addEventListener("click", () => update(button.dataset.sample)));
    $("[data-print]")?.addEventListener("click", () => window.print());
    update("forord");
  }

  function parseCSV(source) {
    const rows = [];
    let row = [];
    let field = "";
    let quoted = false;
    for (let i = 0; i < source.length; i += 1) {
      const ch = source[i];
      if (quoted) {
        if (ch === '"' && source[i + 1] === '"') { field += '"'; i += 1; }
        else if (ch === '"') quoted = false;
        else field += ch;
      } else if (ch === '"') quoted = true;
      else if (ch === ";") { row.push(field); field = ""; }
      else if (ch === "\n") { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; }
      else field += ch;
    }
    if (field || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
    return rows;
  }

  async function initCoverage() {
    const select = $("#coverage-subject");
    const table = $("[data-coverage-table]");
    if (!select || !table) return;
    try {
      const response = await fetch("data/faglige_maal_med_kapiteldaekning.csv");
      if (!response.ok) throw new Error("Fagdata kunne ikke indlæses.");
      const rows = parseCSV(await response.text());
      const header = rows[0] || [];
      const data = rows.slice(1).filter((row) => row.length > 2 && row[0]);
      const subjects = [...new Set(data.map((row) => row[0]).filter(Boolean))];
      select.replaceChildren(...subjects.map((subject) => {
        const option = document.createElement("option");
        option.value = subject;
        option.textContent = subject;
        return option;
      }));
      const render = () => {
        const chosen = data.filter((row) => row[0] === select.value);
        const head = document.createElement("thead");
        const hr = document.createElement("tr");
        for (const label of ["Område", "Vurdering", "Kapitler", "Målet beskriver, at eleverne skal kunne"] ) {
          const th = document.createElement("th"); th.scope = "col"; th.textContent = label; hr.append(th);
        }
        head.append(hr);
        const body = document.createElement("tbody");
        let full = 0; let partial = 0; let none = 0;
        for (const row of chosen) {
          const cells = [document.createElement("td"), document.createElement("td"), document.createElement("td"), document.createElement("td")];
          cells[0].textContent = row[1] || "Fagligt mål";
          const statuses = row.slice(3, 18);
          let mark = statuses.includes("Hele") || statuses.includes("Helt") || statuses.includes("Fuldt") ? "Helt" : statuses.includes("Delvist") ? "Delvist" : "Slet ikke";
          if (mark === "Helt") full += 1; else if (mark === "Delvist") partial += 1; else none += 1;
          const pill = document.createElement("span");
          pill.className = `coverage-pill ${mark === "Helt" ? "full" : mark === "Delvist" ? "partial" : "none"}`;
          pill.textContent = mark;
          cells[1].append(pill);
          const chapterLabels = header.slice(3, 18);
          const covered = statuses.map((status, index) => ({ status, label: chapterLabels[index] })).filter((item) => item.status && item.status !== "Slet ikke");
          cells[2].textContent = covered.length ? covered.map((item) => item.label.replace("Kapitel ", "Kap. ")).join(", ") : "Ingen kapitler markeret";
          cells[3].textContent = row[2] || "";
          const tr = document.createElement("tr"); cells.forEach((cell) => tr.append(cell)); body.append(tr);
        }
        const result = document.createElement("table"); result.className = "coverage-table"; result.append(head, body); table.replaceChildren(result);
        text("[data-coverage-count]", `${chosen.length} mål · ${full} helt · ${partial} delvist · ${none} uden markering`);
      };
      select.addEventListener("change", render);
      render();
    } catch {
      table.textContent = "Fagdata kunne ikke indlæses. Se kildedokumentationen i projektmappen for fag og kapitelkoblinger.";
      select.replaceChildren();
    }
  }

  async function initCoursePlanner() {
    const form = $("[data-course-planner]");
    const chaptersRoot = $("[data-course-chapters]");
    if (!form || !chaptersRoot) return;
    try {
      const chapters = await readJSON("data/chapters.json");
      const fragment = document.createDocumentFragment();
      chapters.forEach((chapter) => {
        const label = document.createElement("label");
        const input = document.createElement("input");
        input.type = "checkbox"; input.name = "chapters"; input.value = chapter.number;
        input.checked = ["01", "02", "03", "04", "05"].includes(chapter.number);
        const span = document.createElement("span"); span.textContent = `${chapter.number} · ${chapter.title}`;
        label.append(input, span); fragment.append(label);
      });
      chaptersRoot.replaceChildren(fragment);
      form.addEventListener("submit", (event) => {
        event.preventDefault();
        const values = new FormData(form);
        const selected = chapters.filter((chapter) => [...values.getAll("chapters")].includes(chapter.number));
        if (!selected.length) {
          const first = $("input[name=chapters]", form);
          first?.focus();
          alert("Vælg mindst ét kapitel til planen.");
          return;
        }
        text("[data-preview-title]", values.get("title")?.toString().trim() || "Undervisningsplan");
        text("[data-preview-subject]", values.get("subject")?.toString().trim() || "Ikke angivet");
        text("[data-preview-length]", values.get("length")?.toString().trim() || "Tilpasses");
        const list = $("[data-preview-chapters]");
        list.replaceChildren(...selected.map((chapter) => { const item = document.createElement("li"); item.textContent = `${chapter.title} — ${chapter.description}`; return item; }));
        const preview = $("[data-print-preview]"); preview.hidden = false;
        preview.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "center" });
      });
      $("[data-print-plan]")?.addEventListener("click", () => window.print());
    } catch {
      chaptersRoot.textContent = "Kapiteldata kunne ikke indlæses. Start hjemmesiden fra en lokal HTTP-server.";
    }
  }

  initMenu();
  initCodeDemo();
  initChapterSearch();
  initLabs();
  initScenarios();
  initLightbox();
  initReader();
  initCoverage();
  initCoursePlanner();
})();
