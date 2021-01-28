$(() => {
    $("#terminal").click(() => {
        layer.open({
            type: 2,
            title: 'Terminal',
            shadeClose: true,
            shade: false,
            maxmin: true,
            area: ['800px', '600px'],
            content: '/internal/terminal_page/' + pid
        })
    })
})