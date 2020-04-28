import {Observable} from "rxjs/index";
import {map} from "rxjs/internal/operators";
import {HttpClient} from "@angular/common/http";
import {Injectable} from "@angular/core";
import {Pizza} from "./pizza.model";

@Injectable()
export class PizzaService {
  private pizzasUrl = 'http://localhost:8080/api/pizzas';

  constructor(private httpClient: HttpClient) {

  }

  getPizzas(): Observable<Pizza[]> {
    return this.httpClient.get<Array<Pizza>>(this.pizzasUrl);
  }

  getPizza(id: number): Observable<Pizza> {
    return this.getPizzas().pipe(map(pizzas => pizzas.find(pizza => pizza.id === id)));
  }
}
