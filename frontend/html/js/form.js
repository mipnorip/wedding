document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('form');

    form.onsubmit = (event) => {
        const name = form.name.value;
        const phone = form.phone.value;

        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
            "name": name,
            "phone": phone
        });

        var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
        };

        fetch('/send', requestOptions)
            .then(response => response.text())
            .then(result => {
                alert("Мы с вами свяжемся");
            })
            .catch(error => console.log('error', error));

        return false;
    }
});

