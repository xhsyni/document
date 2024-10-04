document.addEventListener('DOMContentLoaded', function () {
    const runFileButton = document.getElementById('runFileButton')
    const loadingPart = document.getElementById('loading')
    const form = document.getElementById('email-form');

    runFileButton.addEventListener('click', function (event) {
        event.preventDefault()

        if (form.checkValidity()) {
            runFileButton.style.display = "None"
            loadingPart.style.display = 'block';
            form.submit();
        } else {
            form.reportValidity();
        }
    })

    const filterBySelect = document.getElementById('filterBy')
    const valueField = document.getElementById('value')
    function checkFilter() {
        const filterBy = filterBySelect.value
        if (filterBy === 'all') {
            valueField.removeAttribute('required')
            valueField.setAttribute('disabled', 'disabled')
        } else {
            valueField.removeAttribute('disabled')
            valueField.setAttribute('required', 'required')
        }
    }
    checkFilter()
    filterBySelect.addEventListener('change', checkFilter)

})