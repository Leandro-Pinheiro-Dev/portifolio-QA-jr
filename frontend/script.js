document
  .getElementById("formTinta")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    const feedback = document.getElementById("feedback");
    feedback.textContent = "";
    feedback.className = "";

    const data = {
      nome: document.getElementById("nome").value.trim(),
      tipo: document.getElementById("tipo").value,
      cor: document.getElementById("cor").value,
      acabamento: document.getElementById("acabamento").value,
      quantidade: Number(document.getElementById("quantidade").value),
      validade: document.getElementById("validade").value,
      condicao: document.getElementById("condicao").value,
    };

    if (!data.nome || !data.tipo || !data.cor || data.quantidade <= 0) {
      feedback.textContent =
        "Preencha corretamente todos os campos obrigatórios.";
      feedback.className = "error";
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/cadastrar_tinta", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();

      if (response.ok) {
        feedback.textContent =
          result.message || "Tinta cadastrada com sucesso!";
        feedback.className = "success";
        document.getElementById("formTinta").reset();
      } else {
        feedback.textContent = result.error || "Erro ao cadastrar tinta.";
        feedback.className = "error";
      }
    } catch (error) {
      console.error(error);
      feedback.textContent = "Erro ao conectar com o servidor.";
      feedback.className = "error";
    }
  });
