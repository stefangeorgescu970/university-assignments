import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Author} from './author.model';
import {Observable} from 'rxjs';
import {map} from 'rxjs/internal/operators';

@Injectable()
export class AuthorService {
  private authorsUrl = 'http://localhost:8080/api/authors';

  constructor(private httpClient: HttpClient) {

  }

  getAuthors(): Observable<Author[]> {
    return this.httpClient.get<Array<Author>>(this.authorsUrl);
  }

  getAuthor(id: number): Observable<Author> {
    return this.getAuthors().pipe(map(authors => authors.find(author => author.id === id)));
  }
}
