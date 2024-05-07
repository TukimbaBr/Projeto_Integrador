// Seleciona a barra lateral, o botão de fechar e o botão de busca
let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");

// Adiciona um evento de clique ao botão de fechar
closeBtn.addEventListener("click", ()=>{
    // Alterna a classe "open" na barra lateral para abrir ou fechar
    sidebar.classList.toggle("open");
    // Chama a função para alterar o ícone do botão de fechar
    menuBtnChange();
});

// Adiciona um evento de clique ao botão de busca
searchBtn.addEventListener("click", ()=>{ 
    // Alterna a classe "open" na barra lateral para abrir ou fechar
    sidebar.classList.toggle("open");
    // Chama a função para alterar o ícone do botão de fechar
    menuBtnChange();
});

// Função para alterar o ícone do botão de fechar
function menuBtnChange() {
    // Verifica se a barra lateral está aberta
    if(sidebar.classList.contains("open")){
        // Se estiver aberta, substitui o ícone do botão de fechar pelo ícone de seta
        closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
    } else {
        // Se estiver fechada, substitui o ícone do botão de fechar pelo ícone de menu
        closeBtn.classList.replace("bx-menu-alt-right","bx-menu");
    }
}
