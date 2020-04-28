
import {IngredientService} from "../shared/ingredient.service";
import {Ingredient} from "../shared/ingredient.model";
import {Component, OnInit} from "@angular/core";
import {ActivatedRoute, Params} from "@angular/router";
import {switchMap} from "rxjs/internal/operators";
import {PizzaService} from "../../pizzas/shared/pizza.service";

@Component({
  moduleId: module.id,
  selector: 'app-ingredient-list',
  templateUrl: './ingredient-list.component.html',
  styleUrls: ['./ingredient-list.component.css'],
})

export class IngredientListComponent implements OnInit {
  errorMessage: string;
  ingredients: Array<Ingredient>;

  constructor(private ingredientService: IngredientService,
              private pizzaService: PizzaService,
              private route: ActivatedRoute) {

  }

  ngOnInit(): void {
    this.route.params.pipe(switchMap((params: Params) => this.pizzaService.getPizza(+params['id'])))
      .subscribe(pizza => this.getIngredientsForPizza(pizza.id));
  }

  getIngredientsForPizza(id: number): void {
    this.ingredientService.getIngredientsForPizza(id).subscribe(
      ingredients => this.ingredients = ingredients,
      error => this.errorMessage = <any>error
    );
  }
}
