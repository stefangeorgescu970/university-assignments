import {Component, Input, OnInit} from '@angular/core';
import {Book} from '../shared/book.model';
import {BookService} from '../shared/book.service';
import {ActivatedRoute, Params} from '@angular/router';
import {switchMap} from 'rxjs/internal/operators';
import {AuthorService} from '../../authors/shared/author.service';

@Component({
  moduleId: module.id,
  selector: 'app-books-list',
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.css'],
})

export class BookListComponent implements OnInit {
  errorMessage: string;
  books: Array<Book>;

  constructor(private bookService: BookService,
              private authorService: AuthorService,
              private route: ActivatedRoute) {

  }

  ngOnInit(): void {
    this.route.params.pipe(switchMap((params: Params) => this.authorService.getAuthor(+params['id'])))
      .subscribe(author => this.getBooksByAuthor(author.id));
  }

  getBooksByAuthor(id: number): void {
    this.bookService.getBooksByAuthor(id).subscribe(
      books => this.books = books,
      error => this.errorMessage = <any>error
    );
  }
}
