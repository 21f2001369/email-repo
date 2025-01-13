// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", function () {
    // Select all <div> elements with class "foo" inside a hidden div
    const divs = document.querySelectorAll('.hidden .foo');
    
    // Initialize sum variable
    let sum = 0;
    
    // Loop through each div and add its data-value to the sum
    divs.forEach(div => {
        const value = div.getAttribute('data-value');
        
        // Ensure value is numeric and add it to the sum
        if (value !== null && !isNaN(value)) {
            sum += parseInt(value, 10);
        }
    });
    
    // Output the sum result to the page
    document.getElementById("sumResult").textContent = sum;
});
