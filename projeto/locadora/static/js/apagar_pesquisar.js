$(document).ready(function(){

    var deletebtn = $('.delete-btn');
    var searchbtn = $('#search-btn');
    var searchform = $('#search-form');

    $(deletebtn).on('click' , function(e){

        e.preventDefault();
        var deleteLink = $(this).attr('href');
        var resultado = confirm("Deseja realmente deletar ?");

        if(resultado){
            window.location.href = deleteLink;
        }

    });

    $(searchbtn).on('click' , function(){
        searchform.submit();
    });
});