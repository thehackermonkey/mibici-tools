##Rutas para scrapping

> https://amg.bktbp.com/usuario/
    >LOGIN
    >input#usuario , name = 'usuario'  (#usuario.value = 'youremail@gmail.com')
    >input#pass, name = 'pass' (#pass.value = 'y0urp4ssw0rd')
    >button#autentificacion (#autentificacion.click())

###Una vez logeado

>#myTrips.click() (because fuck url-based navigation)
>#tableContainer >tbody >tr(un viaje)
