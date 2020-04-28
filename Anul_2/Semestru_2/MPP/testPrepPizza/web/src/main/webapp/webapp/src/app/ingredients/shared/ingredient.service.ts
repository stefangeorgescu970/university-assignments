import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs/index";
import {Ingredient} from "./ingredient.model";
import {map} from "rxjs/internal/operators";

@Injectable()
export class IngredientService {
  private ingredientsUrl = 'http://localhost:8080/api/ingredients';

  constructor(private httpClient: HttpClient) {

  }

  getIngredients(): Observable<Ingredient[]> {
    return this.httpClient.get<Array<Ingredient>>(this.ingredientsUrl);
  }

  getIngredientsForPizza(id: number): Observable<Ingredient[]> {
    return this.httpClient.get<Array<Ingredient>>(`${this.ingredientsUrl}/${id}`);
  }

  getIngredient(id: number): Observable<Ingredient> {
    return this.getIngredients().pipe(map(ingredients => ingredients.find(ingredient => ingredient.id === id)));
  }
}
