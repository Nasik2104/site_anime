function updateColor(selectElement) {
    const selectedOption = selectElement.options[selectElement.selectedIndex].value;

    selectElement.classList.remove('favourite-option', 'plans-option', 'watch-option', 'abandoned-option');

    if (selectedOption === 'favourite') {
        selectElement.classList.add('favourite-option');
    } else if (selectedOption === 'plans') {
        selectElement.classList.add('plans-option');
    } else if (selectedOption === 'watch') {
        selectElement.classList.add('watch-option');
    } else if (selectedOption === 'abandoned') {
        selectElement.classList.add('abandoned-option');
    }
}