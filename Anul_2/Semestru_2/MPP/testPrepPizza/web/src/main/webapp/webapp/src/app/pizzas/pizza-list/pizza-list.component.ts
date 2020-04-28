
import {PizzaService} from "../shared/pizza.service";
import {Component, OnInit} from "@angular/core";
import {Router} from "@angular/router";
import {Pizza} from "../shared/pizza.model";

@Component({
  moduleId: module.id,
  selector: 'app-pizza-list',
  templateUrl: './pizza-list.component.html',
  styleUrls: ['./pizza-list.component.css'],
})

export class PizzaListComponent implements OnInit {
  errorMessage: string;
  pizzas: Array<Pizza>;

  constructor(private pizzaService: PizzaService,
              private router: Router) {

  }

  ngOnInit(): void {
    this.getAuthors();
  }

  getAuthors() {
    this.pizzaService.getPizzas().subscribe(
      pizzas => this.pizzas = pizzas,
      error => this.errorMessage = <any>error
    );
  }

  onSelect(pizza: Pizza): void {
    this.router.navigate(['pizzas/detail', pizza.id]);
  }
}
