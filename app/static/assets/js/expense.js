// get all elements

var edit_title = document.getElementById("edit_title");
var edit_category = document.getElementById("edit_category");
var edit_vendor = document.getElementById("edit_vendor");
var edit_date = document.getElementById("edit_date");
var edit_remarks = document.getElementById("edit_remarks");
var edit_amount = document.getElementById("edit_amount");
var edit_currency = document.getElementById('edit_currency');

var new_title = document.getElementById("new_title");
var new_category = document.getElementById("new_category");
var new_vendor = document.getElementById("new_vendor");
var new_date = document.getElementById("new_date");
var new_remarks = document.getElementById("new_remarks");
var new_amount = document.getElementById("new_amount");
var new_currency = document.getElementById('new_currency');

var formValidStatus = false;

var new_titleValidator = document.getElementById("v_new_title");
var new_categoryValidator = document.getElementById("v_new_category");
var new_vendorValidator = document.getElementById("v_new_vendor");
var new_dateValidator = document.getElementById("v_new_date");
var new_remarksValidator = document.getElementById("v_new_remarks");
var new_amountValidator = document.getElementById("v_new_amount");
var new_currencyValidator = document.getElementById('v_new_currency');

class textInputFieldElement {
    constructor(input, validator, validatorType) {
        this.inputElement = input;
        this.inputValidator = validator;
        this.validatorType = validatorType;
    }
    validateText(min, max) {
        //console.log("Validate text is called from Inside");
        var value = this.inputElement.value;
        //console.log(this);
        var returnString = "";
        if (this.validatorType == 'text') {
            if (value.length > max || value.length < min) {
                returnString = "Enter:" + min + "-" + max + "Characters";
                //console.log(this.inputValidator);
                this.inputValidator.textContent = returnString;
                this.inputValidator.style.color = 'red';
                return false;

            } else {
                returnString = "OK";
                this.inputValidator.textContent = returnString;
                this.inputValidator.style.color = 'green';
                return true;
            }
        }

    }


}

class dataListInputElement {

    constructor(input, dataList, validator) {
        this.inputElement = input;
        this.dataList = dataList;
        this.validator = validator;
    }


    validateInput() {
        var value = this.inputElement.value;
        var optionValues = [];
        var returnString = "";
        for (var i = 0; i < this.dataList.options.length; i++) {
            optionValues.push(this.dataList.options[i].value);
        }
        if (optionValues.includes(value)) {
            returnString = "OK";
            this.validator.textContent = returnString;
            this.validator.style.color = 'green';
            return true;
        } else {
            returnString = "Select from Options";
            this.validator.textContent = returnString;
            this.validator.style.color = 'red';
            return false;
        }

    }


}

class dateInputElement {

    constructor(input, validator) {
        this.inputElement = input;
        this.validator = validator;
    }

    validateInput() {
        //console.log(this.inputElement.value, "Date selected");
        var today = new Date();
        var inputDate = new Date(Date.parse(this.inputElement.value));
        var returnString = "";
        var pass = true;
        //console.log(inputDate, today);
        if (inputDate.getDate() < today.getDate() || inputDate.getDate() == today.getDate()) {

            //pass = true;
        } else {
            //console.log("Out of Range Date");
            pass = false;
        }
        if (inputDate.getMonth() < today.getMonth() || inputDate.getMonth() == today.getMonth()) {

            //pass = true;

        } else {
            pass = false;
        }

        if (inputDate.getYear() < today.getYear() || inputDate.getYear() == today.getYear()) {

            //pass = true;

        } else {
            pass = false;
        }

        if (pass) {
            returnString = "Superb!";
            this.validator.textContent = returnString;
            this.validator.style.color = 'green';
            return true;

        } else {

            returnString = "Future Date";
            this.validator.textContent = returnString;
            this.validator.style.color = 'red';
            return false;
        }
    }
}

class NumberValidator {

    constructor(input, validator) {
        this.inputElement = input;
        this.validator = validator;
    }

    checkNegative(number) {
        if (number > 0) {
            return true;
        } else {
            return false;
        }
    }

    validateNumber() {
        var pass = false;
        var inputText = this.inputElement.value;
        var returnString = "";
        if (isNaN(inputText)) {
            returnString = "Number please!";
            this.validator.textContent = returnString;
            this.validator.style.color = 'red';
            return false;
        } else {
            if (this.checkNegative(inputText)) {
                returnString = "Yes!";
                this.validator.textContent = returnString;
                this.validator.style.color = 'green';
                return true;

            } else {
                returnString = "Number>0!";
                this.validator.textContent = returnString;
                this.validator.style.color = 'red';
                return false;
            }

        }
    }
}

function DatetoStringNow() {

    const months = [
        '01',
        '02',
        '03',
        '04',
        '05',
        '06',
        '07',
        '08',
        '09',
        '10',
        '11',
        '12'
    ]
    var today = new Date();
    var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate()


    return date;

}