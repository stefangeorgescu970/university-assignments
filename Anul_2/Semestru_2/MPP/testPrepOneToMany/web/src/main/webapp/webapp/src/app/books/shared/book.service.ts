import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Book} from './book.model';
import {Observable} from 'rxjs/index';
import {filter, map} from 'rxjs/internal/operators';
import index from '@angular/cli/lib/cli';

@Injectable()
export class BookService {
  private booksUrl = 'http://localhost:8080/api/books';

  constructor(private httpClient: HttpClient) {

  }

  getBooks(): Observable<Book[]> {
    return this.httpClient.get<Array<Book>>(this.booksUrl);
  }

  getBooksByAuthor(id: number): Observable<Book[]> {
    return this.httpClient.get<Array<Book>>(`${this.booksUrl}/${id}`);
  }

  getBook(id: number): Observable<Book> {
    return this.getBooks().pipe(map(books => books.find(book => book.id === id)));
  }

  create(isbn: string, title: string, year: number, author: number): Observable<Book> {
    const book = {isbn, title, year, author};
    return this.httpClient.post<Book>(this.booksUrl, book);
  }
}
