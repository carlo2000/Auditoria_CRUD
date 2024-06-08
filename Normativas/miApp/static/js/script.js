document.addEventListener("DOMContentLoaded", function() {
    // Tu código JavaScript aquí
    document.getElementById("mostrarTabla").addEventListener("click", function() {
        document.getElementById("tablaContainer").style.display = "block";
    });
    
    document.getElementById("ocultarTabla").addEventListener("click", function() {
        document.getElementById("tablaContainer").style.display = "none";
    });
});
