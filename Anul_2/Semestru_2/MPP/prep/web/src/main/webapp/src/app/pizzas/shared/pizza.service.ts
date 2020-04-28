import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/index';
import {filter, map} from 'rxjs/internal/operators';
import {Pizza} from "./pizza.model";


@Injectable()
export class PizzaService {
  private pizzasUrl = 'http://localhost:8080/api/pizzas';

  constructor(private httpClient: HttpClient) {

  }

  getPizzas(): Observable<Pizza[]> {
    return this.httpClient.get<Array<Pizza>>(this.pizzasUrl);
  }

  getFilteredPizzas(byPrice: boolean, price: number, byCuisine: boolean, cuisine: string): Observable<Pizza[]> {
    const args = {byPrice, price, byCuisine, cuisine};
    return this.httpClient.post<Array<Pizza>>(`${this.pizzasUrl}/filter`, args);
  }

  createPizza(name: string, description: string, price: number, cuisine: string): Observable<Pizza> {
    const pizza = {name, description, price, cuisine};
    return this.httpClient.post<Pizza>(this.pizzasUrl, pizza);
  }


}
