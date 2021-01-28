$(() => {
    $("#submit").click(() => {
        $.post("/login", { u: $("#user").val(), p: $("#pass").val() }, (d) => {
            if (d == "ok") {
                window.location.href="/internal/list"
            } else {
                alert(d)
            }
        })
    })
})