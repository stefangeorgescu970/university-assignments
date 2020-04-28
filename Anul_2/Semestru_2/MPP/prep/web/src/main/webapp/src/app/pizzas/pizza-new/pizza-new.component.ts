import {Component, OnInit} from "@angular/core";
import {PizzaService} from "../shared/pizza.service";
import {Location} from '@angular/common';

@Component({
  selector: 'app-pizza-new',
  templateUrl: './pizza-new.component.html',
  styleUrls: ['./pizza-new.component.css']
})

export class PizzaNewComponent{

  constructor(private pizzaService: PizzaService,
              private location: Location){

  }

  cuisines = ["MEDITERRANEAN","ORIENTAL"];
  selectedCuisine: string;

  save(name, description, price): void {
    this.pizzaService.createPizza(name, description, price, this.selectedCuisine).subscribe(_=> this.refresh());
  }

  refresh(): void {

  }

}

