// Define a CoffeeMaker object to encapsulate the coffee-making process
const CoffeeMaker = {
    boilWater: function() {
        console.log("Boiling water...");
        // Implement boiling water
    },

    grindCoffee: function() {
        console.log("Grinding coffee beans...");
        // Implement grinding coffe
    },

    brewCoffee: function(time, unit) {
        console.log(`Brewing coffee for ${time} ${unit}...`);
        // Implement brewing coffee
    },

    fillMug: function() {
        console.log("Filling mug with coffee...")
        // Implement filling the mug
    },

    drinkCoffee: function() {
        console.log("Sipping coffee...");
        // Implement drinking coffee
    },
};

// Define a Mug object to represent the coffe mug
const Mug = {
    state: "empty",

    isEmpty: function() {
        return this.state == "empty";
    },

    fill: function() {
        console.log("Filling the mug...");
        this.state = "full";
    },

    empty: function() {
        console.log("Emptying this mug...");
        this.state = "empty";
    },
};

// Morning routine function
function wakeUp() {
    const mug = Object.create(Mug); // Create a new mug instance

    CoffeeMaker.boilWater();
    CoffeeMaker.grindCoffee();
    CoffeeMaker.brewCoffee(4, "minutes");
    CoffeeMaker.fillMug();

    while (!mug.isEmpty()) {
        CoffeeMaker.drinkCoffee();
        mug.empty();
    }

    return "awake";
}

// To use the wakeUp function, you would call it like this:
console.log(wakeUp());