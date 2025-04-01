function filterAndSortByKeyword() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var range = sheet.getDataRange();
  var values = range.getValues();
  var backgrounds = range.getBackgrounds(); // Отримуємо кольори клітинок

  var ui = SpreadsheetApp.getUi();
  var response = ui.prompt("Введіть слова для фільтрації (назва нового аркуша, розділені комами):");
  var keywords = response.getResponseText().trim().toLowerCase().split(",").map(function(keyword) {
    return keyword.trim(); // Обрізаємо пробіли
  });
  
  if (keywords.length === 0 || keywords[0] === "") {
    ui.alert("Ви не ввели жодного слова!");
    return;
  }

  var columnIndex = ui.prompt("Введіть номер стовпця для пошуку (1 для A, 2 для B тощо):").getResponseText();
  columnIndex = parseInt(columnIndex) - 1; // Перетворюємо у масивний індекс

  if (isNaN(columnIndex) || columnIndex < 0 || columnIndex >= values[0].length) {
    ui.alert("Невірний номер стовпця!");
    return;
  }

  var filteredData = [];
  var filteredColors = [];
  
  filteredData.push(values[0]); // Додаємо заголовки
  filteredColors.push(backgrounds[0]); // Додаємо кольори заголовків

  for (var i = 1; i < values.length; i++) {
    // Перевіряємо, чи рядок не порожній
    if (values[i].join("").trim() !== "") {
      // Перевіряємо, чи містить рядок хоча б одне з ключових слів
      var containsKeyword = keywords.some(function(keyword) {
        return values[i][columnIndex].toString().toLowerCase().includes(keyword);
      });

      if (containsKeyword) {
        filteredData.push(values[i]);
        filteredColors.push(backgrounds[i]); // Додаємо відповідні кольори
      }
    }
  }

  if (filteredData.length === 1) {
    ui.alert("Немає результатів за запитом: " + keywords.join(", "));
    return;
  }

  // Створюємо новий аркуш з унікальним іменем
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var newSheetName = keywords.join("_").substring(0, 30); // Обмежуємо ім'я до 30 символів
  var newSheet = ss.insertSheet(newSheetName);

  // Сортуємо дані ТА кольори одночасно
  var header = filteredData[0]; // Зберігаємо заголовки
  var headerColors = filteredColors[0];

  var sortableRows = filteredData.slice(1).map((row, index) => {
    return { data: row, color: filteredColors[index + 1] };
  });

  sortableRows.sort((a, b) => {
    return a.data[columnIndex].toString().localeCompare(b.data[columnIndex].toString());
  });

  // Розпаковуємо відсортовані дані
  filteredData = [header].concat(sortableRows.map(item => item.data));
  filteredColors = [headerColors].concat(sortableRows.map(item => item.color));

  // Записуємо відфільтровані дані
  newSheet.getRange(1, 1, filteredData.length, filteredData[0].length).setValues(filteredData);

  // Записуємо відповідні кольори
  newSheet.getRange(1, 1, filteredColors.length, filteredColors[0].length).setBackgrounds(filteredColors);
  
  ui.alert("Дані відфільтровано та збережено в аркуші '" + newSheetName + "' із збереженням кольорів.");
}