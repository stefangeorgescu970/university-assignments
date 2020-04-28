import {PizzaService} from "../shared/pizza.service";
import {ActivatedRoute, Params} from "@angular/router";
import {Pizza} from "../shared/pizza.model";
import {Component, Input, OnInit} from "@angular/core";
import {switchMap} from "rxjs/internal/operators";
import {Location} from '@angular/common';

@Component({
  selector: 'app-pizza-detail',
  templateUrl: './pizza-detail.component.html',
  styleUrls: ['./pizza-detail.component.css']
})

export class PizzaDetailComponent implements OnInit {
  @Input() pizza: Pizza;

  constructor(private pizzaService: PizzaService,
              private route: ActivatedRoute,
              private location: Location) {

  }

  ngOnInit(): void {
    this.route.params.pipe(switchMap((params: Params) => this.pizzaService.getPizza(+params['id'])))
      .subscribe(pizza => this.pizza = pizza);
  }

  goBack(): void {
    this.location.back();
  }
}
