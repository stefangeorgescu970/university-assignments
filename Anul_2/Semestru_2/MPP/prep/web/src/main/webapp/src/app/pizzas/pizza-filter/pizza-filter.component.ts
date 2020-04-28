


import {Component} from "@angular/core";
import {PizzaService} from "../shared/pizza.service";
import {Pizza} from "../shared/pizza.model";

@Component({
  selector: 'app-pizza-filter',
  templateUrl: './pizza-filter.component.html',
  styleUrls: ['./pizza-filter.component.css']
})

export class PizzaFilterComponent{
  cuisines = ["MEDITERRANEAN","ORIENTAL"];
  selectedCuisine: string;
  isListViewVisible = false;
  errorMessage: string;
  pizzas: Array<Pizza>;

  constructor(private pizzaService: PizzaService){

  }

  getPizzas() {
    this.pizzaService.getPizzas().subscribe(
      pizzas => this.pizzas = pizzas,
      error => this.errorMessage = <any>error
    );
  }

  getFilteredPizzas(byPrice: boolean, price: number, byCuisine: boolean, cuisine: string){
    this.pizzaService.getFilteredPizzas(byPrice, price, byCuisine, cuisine).subscribe(
      pizzas => this.pizzas = pizzas,
      error => this.errorMessage = <any>error);
  }

  showResults(price: number) {
    const priceCheckBox = <HTMLInputElement> document.getElementById("priceCheckBox");
    const filterByPrice = priceCheckBox.checked;

    const cuisineCheckBox = <HTMLInputElement> document.getElementById("cuisineCheckBox");
    const filterByCuisine = cuisineCheckBox.checked;

    this.isListViewVisible = true;

    this.getFilteredPizzas(filterByPrice, price, filterByCuisine, this.selectedCuisine);
  }
}
