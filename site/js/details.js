// JavaScript Document
$(document).ready(function () {
    var data, grid, dialog;
    data = [
        { "ID": 1, "Name": "Hristo Stoichkov", "PlaceOfBirth": "Plovdiv, Bulgaria" },
        { "ID": 2, "Name": "Ronaldo Luís Nazário de Lima", "PlaceOfBirth": "Rio de Janeiro, Brazil" },
        { "ID": 3, "Name": "David Platt", "PlaceOfBirth": "Chadderton, Lancashire, England" }
    ];
    dialog = $("#dialog").dialog({
        title: "Add/Edit Record",
        autoOpen: false,
        resizable: false,
        modal: true,
        buttons: {
            "Save": Save,
            "Cancel": function () { $(this).dialog("close"); }
        }
    });
    function Edit(e) {
        $("#ID").val(e.data.id);
        $("#Name").val(e.data.record.Name);
        $("#PlaceOfBirth").val(e.data.record.PlaceOfBirth);
        $("#dialog").dialog("open");
    }
    function Delete(e) {
        if (confirm("Are you sure?")) {
            grid.removeRow(e.data.id);
        }
    }
    function Save() {
        if ($("#ID").val()) {
            var id = parseInt($("#ID").val());
            grid.updateRow(id, { "ID": id, "Name": $("#Name").val(), "PlaceOfBirth": $("#PlaceOfBirth").val() });
        } else {
            grid.addRow({ "ID": grid.count() + 1, "Name": $("#Name").val(), "PlaceOfBirth": $("#PlaceOfBirth").val() });
        }
        $(this).dialog("close");
    }
    grid = $("#grid").grid({
        dataSource: data,
        columns: [
            { field: "ID" },
            { field: "Name" },
            { field: "PlaceOfBirth", title: "Place Of Birth" },
            { title: "", width: 20, type: "icon", icon: "ui-icon-pencil", tooltip: "Edit", events: { "click": Edit } },
            { title: "", width: 20, type: "icon", icon: "ui-icon-close", tooltip: "Delete", events: { "click": Delete } }
        ]
    });
    $("#btnAdd").on("click", function () {
        $("#ID").val("");
        $("#Name").val("");
        $("#PlaceOfBirth").val("");
        $("#dialog").dialog("open");
    });
});