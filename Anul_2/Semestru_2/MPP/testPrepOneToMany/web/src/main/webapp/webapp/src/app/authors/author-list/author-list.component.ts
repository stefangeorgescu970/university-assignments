import {Component, OnInit} from '@angular/core';
import {Author} from '../shared/author.model';
import {Router} from '@angular/router';
import {AuthorService} from '../shared/author.service';

@Component({
  moduleId: module.id,
  selector: 'app-authors-list',
  templateUrl: './author-list.component.html',
  styleUrls: ['./author-list.component.css'],
})

export class AuthorListComponent implements OnInit {
  errorMessage: string;
  authors: Array<Author>;
  selectedAuthor: Author;

  constructor(private authorService: AuthorService,
              private router: Router) {

  }

  ngOnInit(): void {
    this.getAuthors();
  }

  getAuthors() {
    this.authorService.getAuthors().subscribe(
      authors => this.authors = authors,
      error => this.errorMessage = <any>error
    );
  }

  onSelect(author: Author): void {
    this.selectedAuthor = author;
}

  goToDetail(): void {
    this.router.navigate(['authors/detail', this.selectedAuthor.id]);
  }
}
