document.addEventListener('DOMContentLoaded', function() {
    const elementoDados = document.getElementById('dados-grafico');
    
    if (elementoDados) {
        // Captura os dados que o Flask enviou para o HTML
        const energia = elementoDados.getAttribute('data-energia');
        const agua = elementoDados.getAttribute('data-agua');
        const co2 = elementoDados.getAttribute('data-co2');

        const ctx = document.getElementById('meuGrafico').getContext('2d');
        
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Energia (kWh)', 'Água (L)', 'CO2 (kg)'],
                datasets: [{
                    label: 'Economia Realizada',
                    data: [energia, agua, co2],
                    backgroundColor: ['#4CAF50', '#2196F3', '#FF9800'],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    }
});