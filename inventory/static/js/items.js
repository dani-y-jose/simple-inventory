let dataTable;
let dataTableIsInitialized = false;
const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6] },
        { orderable: false, targets: [5, 6] },
        { searchable: false, targets: [0, 2, 5, 6] },
    ],
    pageLength: 2,

}
const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listItems();

    dataTable = $('#datatable-items').DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};


const listItems = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/inventory/list_items/');
        const data = await response.json();

        let content = ``;
        data.items.forEach((item, index) => {
            content += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${item.model}</td>
                    <td>${item.brand}</td>
                    <td>${item.quantity}</td>
                    <td>${item.description}</td>
                    <td>${item.location_id}</td>
                    <td>${item.item_status_id}</td>
                </tr>
            `;
        });
        tableBody_items.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});