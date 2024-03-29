/*
Template Name: Admiria - Admin & Dashboard Template
Author: Themesbrand
Website: https://themesbrand.com/
Contact: themesbrand@gmail.com
File: Datatables Js File
*/

$(document).ready(function() {
    $('#datatable').DataTable();

    //Варианты действий с выбранными абонентами (отмеченными Checkbox-ми)
    var table = $('#datatable-buttons').DataTable({
        lengthChange: false,
        buttons: ['excel', 'pdf']
        //buttons: ['copy', 'excel', 'pdf', 'colvis']
    });

    table.buttons().container()
        .appendTo('#datatable-buttons_wrapper .col-md-6:eq(0)');

        $(".dataTables_length select").addClass('form-select form-select-sm');
} );

