import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Book} from './book.model';
import {Observable} from 'rxjs/index';
import {filter, map} from 'rxjs/internal/operators';
import index from '@angular/cli/lib/cli';
import {BookWithData} from "./bookWithData.model";

@Injectable()
export class BookService {
  private booksUrl = 'http://localhost:8080/api/books';

  constructor(private httpClient: HttpClient) {

  }

  getBooks(): Observable<BookWithData[]> {
    return this.httpClient.get<Array<Book>>(this.booksUrl);
  }

  getBooksByAuthor(id: number): Observable<Book[]> {
    return this.httpClient.get<Array<Book>>(`${this.booksUrl}/${id}`);
  }

  getBooksByAuthorAndYear(authorId: number, year: number): Observable<BookWithData[]> {
    return this.httpClient.get<Array<BookWithData>>(`${this.booksUrl}?authorId=${authorId}&year=${year}`);
  }
}
